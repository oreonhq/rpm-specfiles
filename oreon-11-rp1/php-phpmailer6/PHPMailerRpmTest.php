<?php
/**
 * PHPMailer - RPM language file tests.
 */

namespace PHPMailer\Test;

use PHPMailer\PHPMailer\PHPMailer;
use PHPUnit\Framework\TestCase;

/**
 * Check language files for RPM packaging
 */
final class PHPMailerRpmTest extends TestCase
{
    /**
     * Holds a PHPMailer instance.
     *
     * @var PHPMailer
     */
    private $Mail;

    /**
     * Run before each test is started.
     */
    protected function setUp(): void
    {
        $this->Mail = new PHPMailer();
    }

    public function testTranslation()
    {
        $this->Mail->setLanguage();
        $tr = $this->Mail->getTranslations();
        $this->assertEquals('Message body empty', $tr['empty_message'], "English message");

        $this->Mail->setLanguage('fr');
        $tr = $this->Mail->getTranslations();
        $this->assertEquals('Corps du message vide.', $tr['empty_message'], "French message");
    }
}
