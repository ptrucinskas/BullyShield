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
        $token = $this->get('security.token_storage')->getToken();

        if(!$token->getUser()) {
            /*
             *  If User not authenticated
             */
            return $this->redirectToRoute('fos_user_security_login');
        }else{
            /*
             *  If User authenticated
             */
            return $this->redirectToRoute('fos_message_inbox');
        }
    }
}
