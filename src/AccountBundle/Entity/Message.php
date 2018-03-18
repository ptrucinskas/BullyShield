<?php

namespace AccountBundle\Entity;

use Doctrine\ORM\Mapping as ORM;
use Doctrine\Common\Collections\Collection;
use Doctrine\Common\Collections\ArrayCollection;
use FOS\MessageBundle\Entity\Message as BaseMessage;

/**
 * Message
 *
 * @ORM\Table(name="message")
 * @ORM\Entity(repositoryClass="AccountBundle\Repository\MessageRepository")
 */
class Message extends BaseMessage
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
     * @ORM\ManyToOne(
     *   targetEntity="AccountBundle\Entity\Thread",
     *   inversedBy="messages"
     * )
     * @var \FOS\MessageBundle\Model\ThreadInterface
     */
    protected $thread;

    /**
     * @ORM\ManyToOne(targetEntity="AccountBundle\Entity\User")
     * @var \FOS\MessageBundle\Model\ParticipantInterface
     */
    protected $sender;

    /**
     * @ORM\OneToMany(
     *   targetEntity="AccountBundle\Entity\MessageMetadata",
     *   mappedBy="message",
     *   cascade={"all"}
     * )
     * @var MessageMetadata[]|Collection
     */
    protected $metadata;

    /**
     * @var boolean
     *
     * @ORM\Column(name="flag", type="boolean", options={"default" : false})
     */
    protected $flag;


    /**
     * @var boolean
     *
     * @ORM\Column(name="receiverFlag", type="boolean", options={"default" : false})
     */
    protected $receiverFlag;

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
     * @return Message
     */
    public function setFlag($flag)
    {
        $this->flag = $flag;
        return $this;
    }

    /**
     * Get receiverFlag
     *
     * @return boolean
     */
    public function getReceiverFlag()
    {
        return $this->receiverFlag;
    }

    /**
     * Set receiverFlag
     *
     * @param boolean $receiverFlag
     *
     * @return Message
     */
    public function setReceiverFlag()
    {
        $this->receiverFlag = !($this->receiverFlag);
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

    public function __construct()
    {
        $this->setFlag(false);
        $this->receiverFlag = false;
        $this->createdAt = new \DateTime();
        $this->metadata = new ArrayCollection();
    }
}

