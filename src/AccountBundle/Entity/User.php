<?php

namespace AccountBundle\Entity;


use FOS\UserBundle\Model\User as BaseUser;
use Doctrine\ORM\Mapping as ORM;
use FOS\MessageBundle\Model\ParticipantInterface;
use Symfony\Component\Validator\Constraints as Assert;

/**
 * User
 *
 * @ORM\Table(name="fos_user")
 * @ORM\Entity(repositoryClass="AccountBundle\Repository\UserRepository")
 */
class User extends BaseUser implements ParticipantInterface
{
    /**
     * @var int
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    protected $id;


    /**
     * @var string
     *
     * @ORM\Column(name="guardian", type="string", length=180)
     * @Assert\NotBlank(message="Please enter your guardian's email.", groups={"Registration", "Profile"})
     */
    protected $guardian;

    /**
     * @var boolean
     *
     * @ORM\Column(name="flag", type="boolean", options={"default" : false})
     */
    protected $flag;

    /**
     * Get flag
     *
     * @return boolean
     */
    public function getFlag()
    {
        return $this->flag;
    }

    /**
     * Set flag
     *
     * @param boolean $flag
     *
     * @return User
     */
    public function setFlag($flag)
    {
        $this->flag = $flag;
        return $this;
    }

    /**
     * Get guardian
     *
     * @return string
     */
    public function getGuardian()
    {
        return $this->guardian;
    }

    /**
     * Set guardian
     *
     * @param string $guardian
     *
     * @return User
     */
    public function setGuardian($guardian)
    {
        $this->guardian = $guardian;
        return $this;
    }

    /**
     * Get id
     *
     * @return int
     */
    public function getId()
    {
        return $this->id;
    }
}

