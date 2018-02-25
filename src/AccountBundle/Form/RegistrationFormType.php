<?php
// src/AccountBundle/Form/RegistrationFormType.php

namespace AccountBundle\Form;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use FOS\UserBundle\Util\LegacyFormHelper;
use Symfony\Component\OptionsResolver\OptionsResolver;

class RegistrationFormType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder->add('guardian');//,
       /*     LegacyFormHelper::getType('Symfony\Component\Form\Extension\Core\Type\EmailType'),
            array(
                'label' => 'form.guardian_email',
                'translation_domain' => 'FOSUserBundle'
            )
        );*/
    }

    public function getParent()
    {
        return 'FOS\UserBundle\Form\Type\RegistrationFormType';
    }

    public function getBlockPrefix()
    {
        return 'account_user_registration';
    }

    public function getName()
    {
        return $this->getBlockPrefix();
    }
}