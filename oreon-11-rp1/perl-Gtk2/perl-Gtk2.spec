%global source0_hash 49c443743b2eefe11a768002724f7f6a4c48efc94ff3cd3a559fb7e7b693c967

#
# Rebuild option:
#
#   --with testsuite         - run the test suite (requires X)
#

# We need to manually generate the Provides here, here's the best way I know of:
# for i in `grep -r "PACKAGE = " * | cut -d " " -f 3 | cut -f 1`; do printf "Provides: perl($i)\n" &>>provides.txt; done
# cat provides.txt | sort -n | uniq

Name:           perl-Gtk2
Version:        1.24993
Release:        24%{?dist}
Summary:        Perl interface to the 2.x series of the Gimp Toolkit library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk2-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-interpreter >= 2:5.8.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  gtk2-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Glib) >= 1.240
BuildRequires:	perl(Pango) >= 1.220
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Cairo) >= 1.00
Requires:       perl(Glib) >= 1.240
Requires:       perl(Cairo) >= 1.00
Requires:       perl(Pango) >= 1.220
# Be sure to update this list on any upstream change
Provides: perl(Gtk2)
Provides: perl(Gtk2::AboutDialog)
Provides: perl(Gtk2::AccelGroup)
Provides: perl(Gtk2::AccelLabel)
Provides: perl(Gtk2::AccelMap)
Provides: perl(Gtk2::Action)
Provides: perl(Gtk2::ActionGroup)
Provides: perl(Gtk2::Activatable)
Provides: perl(Gtk2::Adjustment)
Provides: perl(Gtk2::Alignment)
Provides: perl(Gtk2::Arrow)
Provides: perl(Gtk2::AspectFrame)
Provides: perl(Gtk2::Assistant)
Provides: perl(Gtk2::Bin)
Provides: perl(Gtk2::BindingSet)
Provides: perl(Gtk2::Box)
Provides: perl(Gtk2::Buildable)
Provides: perl(Gtk2::Builder)
Provides: perl(Gtk2::Button)
Provides: perl(Gtk2::ButtonBox)
Provides: perl(Gtk2::Calendar)
Provides: perl(Gtk2::CellEditable)
Provides: perl(Gtk2::CellLayout)
Provides: perl(Gtk2::CellRenderer)
Provides: perl(Gtk2::CellRendererAccel)
Provides: perl(Gtk2::CellRendererCombo)
Provides: perl(Gtk2::CellRendererPixbuf)
Provides: perl(Gtk2::CellRendererProgress)
Provides: perl(Gtk2::CellRendererSpin)
Provides: perl(Gtk2::CellRendererSpinner)
Provides: perl(Gtk2::CellRendererText)
Provides: perl(Gtk2::CellRendererToggle)
Provides: perl(Gtk2::CellView)
Provides: perl(Gtk2::CheckButton)
Provides: perl(Gtk2::CheckMenuItem)
Provides: perl(Gtk2::Clipboard)
Provides: perl(Gtk2::ColorButton)
Provides: perl(Gtk2::ColorSelection)
Provides: perl(Gtk2::ColorSelectionDialog)
Provides: perl(Gtk2::Combo)
Provides: perl(Gtk2::ComboBox)
Provides: perl(Gtk2::ComboBoxEntry)
Provides: perl(Gtk2::Constants)
Provides: perl(Gtk2::Container)
Provides: perl(Gtk2::Curve)
Provides: perl(Gtk2::Dialog)
Provides: perl(Gtk2::Dnd)
Provides: perl(Gtk2::DrawingArea)
Provides: perl(Gtk2::Editable)
Provides: perl(Gtk2::Entry)
Provides: perl(Gtk2::EntryBuffer)
Provides: perl(Gtk2::EntryCompletion)
Provides: perl(Gtk2::EventBox)
Provides: perl(Gtk2::Expander)
Provides: perl(Gtk2::FileChooser)
Provides: perl(Gtk2::FileChooserButton)
Provides: perl(Gtk2::FileChooserDialog)
Provides: perl(Gtk2::FileChooserWidget)
Provides: perl(Gtk2::FileFilter)
Provides: perl(Gtk2::FileSelection)
Provides: perl(Gtk2::Fixed)
Provides: perl(Gtk2::FontButton)
Provides: perl(Gtk2::FontSelection)
Provides: perl(Gtk2::Frame)
Provides: perl(Gtk2::GammaCurve)
Provides: perl(Gtk2::GC)
Provides: perl(Gtk2::Gdk)
Provides: perl(Gtk2::Gdk::Cairo)
Provides: perl(Gtk2::Gdk::Color)
Provides: perl(Gtk2::Gdk::Cursor)
Provides: perl(Gtk2::Gdk::Device)
Provides: perl(Gtk2::Gdk::Display)
Provides: perl(Gtk2::Gdk::DisplayManager)
Provides: perl(Gtk2::Gdk::Dnd)
Provides: perl(Gtk2::Gdk::Drawable)
Provides: perl(Gtk2::Gdk::Event)
Provides: perl(Gtk2::Gdk::GC)
Provides: perl(Gtk2::Gdk::Image)
Provides: perl(Gtk2::Gdk::Keys)
Provides: perl(Gtk2::Gdk::Pango)
Provides: perl(Gtk2::Gdk::Pixbuf)
Provides: perl(Gtk2::Gdk::PixbufLoader)
Provides: perl(Gtk2::Gdk::PixbufSimpleAnim)
Provides: perl(Gtk2::Gdk::Pixmap)
Provides: perl(Gtk2::Gdk::Property)
Provides: perl(Gtk2::Gdk::Region)
Provides: perl(Gtk2::Gdk::Rgb)
Provides: perl(Gtk2::Gdk::Screen)
Provides: perl(Gtk2::Gdk::Selection)
Provides: perl(Gtk2::Gdk::Types)
Provides: perl(Gtk2::Gdk::Visual)
Provides: perl(Gtk2::Gdk::Window)
Provides: perl(Gtk2::Gdk::X11)
Provides: perl(Gtk2::HandleBox)
Provides: perl(Gtk2::HBox)
Provides: perl(Gtk2::HButtonBox)
Provides: perl(Gtk2::HPaned)
Provides: perl(Gtk2::HRuler)
Provides: perl(Gtk2::HScale)
Provides: perl(Gtk2::HScrollbar)
Provides: perl(Gtk2::HSeparator)
Provides: perl(Gtk2::HSV)
Provides: perl(Gtk2::IconFactory)
Provides: perl(Gtk2::IconTheme)
Provides: perl(Gtk2::IconView)
Provides: perl(Gtk2::Image)
Provides: perl(Gtk2::ImageMenuItem)
Provides: perl(Gtk2::IMContext)
Provides: perl(Gtk2::IMContextSimple)
Provides: perl(Gtk2::IMMultiContext)
Provides: perl(Gtk2::InfoBar)
Provides: perl(Gtk2::InputDialog)
Provides: perl(Gtk2::Invisible)
Provides: perl(Gtk2::Item)
Provides: perl(Gtk2::ItemFactory)
Provides: perl(Gtk2::Label)
Provides: perl(Gtk2::Layout)
Provides: perl(Gtk2::LinkButton)
Provides: perl(Gtk2::List)
Provides: perl(Gtk2::ListItem)
Provides: perl(Gtk2::ListStore)
Provides: perl(Gtk2::Menu)
Provides: perl(Gtk2::MenuBar)
Provides: perl(Gtk2::MenuItem)
Provides: perl(Gtk2::MenuShell)
Provides: perl(Gtk2::MenuToolButton)
Provides: perl(Gtk2::MessageDialog)
Provides: perl(Gtk2::Misc)
Provides: perl(Gtk2::Notebook)
Provides: perl(Gtk2::Object)
Provides: perl(Gtk2::OffscreenWindow)
Provides: perl(Gtk2::OptionMenu)
Provides: perl(Gtk2::Orientable)
Provides: perl(Gtk2::PageSetup)
Provides: perl(Gtk2::Paned)
Provides: perl(Gtk2::PaperSize)
Provides: perl(Gtk2::Plug)
Provides: perl(Gtk2::PrintContext)
Provides: perl(Gtk2::PrintOperation)
Provides: perl(Gtk2::PrintOperationPreview)
Provides: perl(Gtk2::PrintSettings)
Provides: perl(Gtk2::ProgressBar)
Provides: perl(Gtk2::RadioAction)
Provides: perl(Gtk2::RadioButton)
Provides: perl(Gtk2::RadioMenuItem)
Provides: perl(Gtk2::RadioToolButton)
Provides: perl(Gtk2::Range)
Provides: perl(Gtk2::Rc)
Provides: perl(Gtk2::RecentAction)
Provides: perl(Gtk2::RecentChooser)
Provides: perl(Gtk2::RecentChooserDialog)
Provides: perl(Gtk2::RecentChooserMenu)
Provides: perl(Gtk2::RecentChooserWidget)
Provides: perl(Gtk2::RecentFilter)
Provides: perl(Gtk2::RecentManager)
Provides: perl(Gtk2::Ruler)
Provides: perl(Gtk2::Scale)
Provides: perl(Gtk2::ScaleButton)
Provides: perl(Gtk2::ScrolledWindow)
Provides: perl(Gtk2::Selection)
Provides: perl(Gtk2::SeparatorMenuItem)
Provides: perl(Gtk2::SeparatorToolItem)
Provides: perl(Gtk2::Show)
Provides: perl(Gtk2::SizeGroup)
Provides: perl(Gtk2::Socket)
Provides: perl(Gtk2::SpinButton)
Provides: perl(Gtk2::Spinner)
Provides: perl(Gtk2::Statusbar)
Provides: perl(Gtk2::StatusIcon)
Provides: perl(Gtk2::Stock)
Provides: perl(Gtk2::Style)
Provides: perl(Gtk2::Table)
Provides: perl(Gtk2::TearoffMenuItem)
Provides: perl(Gtk2::TextBuffer)
Provides: perl(Gtk2::TextBufferRichText)
Provides: perl(Gtk2::TextChildAnchor)
Provides: perl(Gtk2::TextIter)
Provides: perl(Gtk2::TextMark)
Provides: perl(Gtk2::TextTag)
Provides: perl(Gtk2::TextTagTable)
Provides: perl(Gtk2::TextView)
Provides: perl(Gtk2::ToggleAction)
Provides: perl(Gtk2::ToggleButton)
Provides: perl(Gtk2::ToggleToolButton)
Provides: perl(Gtk2::Toolbar)
Provides: perl(Gtk2::ToolButton)
Provides: perl(Gtk2::ToolItem)
Provides: perl(Gtk2::ToolItemGroup)
Provides: perl(Gtk2::ToolPalette)
Provides: perl(Gtk2::ToolShell)
Provides: perl(Gtk2::Tooltip)
Provides: perl(Gtk2::Tooltips)
Provides: perl(Gtk2::TreeDnd)
Provides: perl(Gtk2::TreeModel)
Provides: perl(Gtk2::TreeModelFilter)
Provides: perl(Gtk2::TreeModelSort)
Provides: perl(Gtk2::TreeSelection)
Provides: perl(Gtk2::TreeSortable)
Provides: perl(Gtk2::TreeStore)
Provides: perl(Gtk2::TreeView)
Provides: perl(Gtk2::TreeViewColumn)
Provides: perl(Gtk2::UIManager)
Provides: perl(Gtk2::VBox)
Provides: perl(Gtk2::VButtonBox)
Provides: perl(Gtk2::Viewport)
Provides: perl(Gtk2::VolumeButton)
Provides: perl(Gtk2::VPaned)
Provides: perl(Gtk2::VRuler)
Provides: perl(Gtk2::VScale)
Provides: perl(Gtk2::VScrollbar)
Provides: perl(Gtk2::VSeparator)
Provides: perl(Gtk2::Widget)
Provides: perl(Gtk2::Window)

%description
This module allows you to write Gtk+ graphical user interfaces in a
perlish and object-oriented way, freeing you from the casting and
memory management in C, yet remaining very close in spirit to original
API.  Find out more about Gtk+ at http://www.gtk.org.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-%{version}

# iconv -f iso-8859-1 -t utf-8 -o pm/Helper.pm{.utf8,}
# mv pm/Helper.pm{.utf8,}

%build
# gtk2 is not c23 friendly
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS -std=gnu17"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?_with_testsuite:make test}

%files
%doc AUTHORS ChangeLog.pre-git NEWS README TODO
%doc examples/ gtk-demo/
%license LICENSE
%{perl_vendorarch}/auto/Gtk2/
%{perl_vendorarch}/Gtk2*
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
