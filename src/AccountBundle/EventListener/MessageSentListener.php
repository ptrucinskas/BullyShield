<?php

namespace AccountBundle\EventListener;
use Icicle\Coroutine\Coroutine;
use Symfony\Component\Config\Definition\Exception\Exception;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

use AccountBundle\Entity\Message;
use AccountBundle\Entity\Thread;
use Doctrine\ORM\Event\LifecycleEventArgs;

class MessageSentListener
{
    public function postPersist(LifecycleEventArgs $args){
        $entity = $args->getEntity();

        if(!$entity instanceof Message) return;

        $em = $args->getEntityManager();
        $threadId = $entity->getThread()->getId();
        $em->getRepository(Thread::class)->find($threadId)->setLastUpdated();
        $em->flush();

        $id = $entity->getId();
        $userId = $entity->getSender()->getId();
        $pyLoc = "/home/pt/Desktop/GroupProject/web/py/BullyShield.py";
        $process = new Process("python $pyLoc $userId $id");
        $process->start();
        return true;
    }
}