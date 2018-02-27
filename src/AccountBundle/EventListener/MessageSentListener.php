<?php

namespace AccountBundle\EventListener;

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
    }
}