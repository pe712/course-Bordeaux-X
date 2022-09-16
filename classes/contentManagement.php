<?php
class Content
{
    public $page;
    public $section;
    public $sous_section;
    public $contenu;
    public $description;

    public function __construct(
        $page=null,
        $section=null,
        $sous_section=null,
        $contenu=null,
        $description=null
    ) {
        $this->page = $page;
        $this->section = $section;
        $this->sous_section = $sous_section;
        $this->contenu = $contenu;
        $this->description = $description;
    }

    public function update_db($conn)
    {
        $update = $conn->prepare("update content set contenu=? where page=? and section=? and sous_section=?");
        $update->execute(array($this->contenu, $this->page, $this->section, $this->sous_section));
    }
}
