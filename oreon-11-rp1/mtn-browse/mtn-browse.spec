%global source0_hash c14ffaf742ccdc47dad7ad98f2bf93cf01f6a00bfce6ce4c020227b41006a90d

Name:           mtn-browse
Version:        1.20
Release:        23%{?dist}
Summary:        Application for browsing Monotone VCS databases
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.coosoft.plus.com/software.html
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        mtn-browse.desktop
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Gnome2)
BuildRequires:  perl(Gnome2::Canvas)
BuildRequires:  perl(Gnome2::VFS)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::GladeXML)
BuildRequires:  perl(Gtk2::SourceView2)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Monotone::AutomateStdio) >= 1.10
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  meld graphviz
Requires:       meld graphviz
BuildArch:      noarch

%description
Monotone browser (mtn-browse) is an application for browsing Monotone
VCS databases without the need for a work space. The interface allows
one to:
* Easily select a revision from within a branch
* Find a revision using complex queries
* Navigate the contents of a revision using a built in file manager
* Display file contents, either using the internal viewer or an
  external helper application
* Compare the changes between different revisions or versions of a
  file either using the internal difference viewer or an external
  application
* Find files within a revision based on detailed search criteria
* Display file annotations and easily refer back to the corresponding
  change documentation
* Save files to disk

%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{_datadir}/%{name}/perl
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(AdvancedFind\\)
%global __requires_exclude %__requires_exclude|perl\\(Annotate\\)
%global __requires_exclude %__requires_exclude|perl\\(CachingAutomateStdio\\)
%global __requires_exclude %__requires_exclude|perl\\(ChangeLog\\)
%global __requires_exclude %__requires_exclude|perl\\(ComboAutoCompletion\\)
%global __requires_exclude %__requires_exclude|perl\\(Common\\)
%global __requires_exclude %__requires_exclude|perl\\(Completion\\)
%global __requires_exclude %__requires_exclude|perl\\(DateRange\\)
%global __requires_exclude %__requires_exclude|perl\\(FindFiles\\)
%global __requires_exclude %__requires_exclude|perl\\(FindTextAndGoToLine\\)
%global __requires_exclude %__requires_exclude|perl\\(Globals\\)
%global __requires_exclude %__requires_exclude|perl\\(History\\)
%global __requires_exclude %__requires_exclude|perl\\(HistoryGraph\\)
%global __requires_exclude %__requires_exclude|perl\\(LocaleEnableUtf8\\)
%global __requires_exclude %__requires_exclude|perl\\(ManageServerBookmarks\\)
%global __requires_exclude %__requires_exclude|perl\\(ManageTagWeightings\\)
%global __requires_exclude %__requires_exclude|perl\\(MultipleRevisions\\)
%global __requires_exclude %__requires_exclude|perl\\(Preferences\\)
%global __requires_exclude %__requires_exclude|perl\\(WindowManager\\)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# empty

%install
./linux-installer \
  --destdir=%{buildroot} \
  --prefix=%{_prefix} \
  --file-comparison=meld \
  --no-use-dists-mas \
  --libdir=share/%{name}

install -m 644 -D -p \
  ./lib/ui/pixmaps/mtn-browse-small.png \
  %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
