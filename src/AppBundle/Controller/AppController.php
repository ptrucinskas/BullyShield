<?php

namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;

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


    }

    /**
     * @Route("/ajax_update_threads", name="ajax_update_messages")
     */
    public function refreshThreadListAction(Request $request){

    }



}
