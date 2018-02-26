<?php

namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\Config\Definition\Exception\Exception;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use AccountBundle\Entity\Message;
use AccountBundle\Entity\Thread;
use Symfony\Component\Intl\Tests\Data\Provider\Json\JsonRegionDataProviderTest;

class AppController extends Controller
{
    /**
     * @Route("/", name="homepage")
     */
    public function indexAction(Request $request)
    {
        return $this->render("@App/index.html.twig");
    }

    /**
     * @Route("/ajax_update_messages", name="ajax_update_messages")
     */
    public function refreshMessageListAction(Request $request){
        $receivedLastUpdate = $request->request->get('last_update');
        $em = $this->getDoctrine()->getManager();
        $threadLastUpdated = $this->getDoctrine()
            ->getRepository(Thread::class)
            ->find($request->request->get("thread_id"))
            ->getLastUpdated()
            ->format("H/i/s/d/m/Y");
        if($request->request->get('last_update') != $threadLastUpdated){
            return new JsonResponse("Refresh");
        }else{
            return new JsonResponse("Messages up to date");
        }

    }

    /**
     * @Route("/ajax_update_threads", name="ajax_update_threads")
     */
    public function refreshThreadListAction(Request $request){

    }



}
