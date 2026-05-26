Summary: Basic desktop integration functions
Name:    xdg-utils
Version: 1.2.1
Release: 5%{?dist}

URL:     https://www.freedesktop.org/wiki/Software/xdg-utils/
%if 0%{?snap:1}
Source0:        https://gitlab.freedesktop.org/xdg/xdg-utils/-/archive/v1.2.1/xdg-utils-v1.2.1.tar.gz
%else
Source0:  https://gitlab.freedesktop.org/xdg/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 f6b648c064464c2636884c05746e80428110a576f8daacf46ef2e554dcfdae75
%global source0_file xdg-utils-v1.2.1.tar.gz
# oreon url source checksums end
%endif
License: MIT

# make sure BuildArch comes *after* patches, to ensure %%autosetup works right
# http://bugzilla.redhat.com/1084309
BuildArch: noarch

BuildRequires: make
BuildRequires: gawk
BuildRequires: xmlto lynx

Requires: coreutils
Requires: desktop-file-utils
Requires: which

%description
The %{name} package is a set of simple scripts that provide basic
desktop integration functions for any Free Desktop, such as Linux.
They are intended to provide a set of defacto standards.
This means that:
*  Third party software developers can rely on these xdg-utils
   for all of their simple integration needs.
*  Developers of desktop environments can make sure that their
   environments are well supported
*  Distribution vendors can provide custom versions of these utilities

The following scripts are provided at this time:
* xdg-desktop-icon      Install icons to the desktop
* xdg-desktop-menu      Install desktop menu items
* xdg-email             Send mail using the user's preferred e-mail composer
* xdg-icon-resource     Install icon resources
* xdg-mime              Query information about file type handling and
                        install descriptions for new file types
* xdg-open              Open a file or URL in the user's preferred application
* xdg-screensaver       Control the screensaver
* xdg-settings          Get various settings from the desktop environment


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xdg-utils-v1.2.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f6b648c064464c2636884c05746e80428110a576f8daacf46ef2e554dcfdae75" || { echo "oreon: Source0 SHA256 mismatch for xdg-utils-v1.2.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{name}-v%{version} -p1


%build
%configure

%if 0%{?snap:1}
make scripts-clean -C scripts
make man scripts %{?_smp_mflags} -C scripts
%endif
%make_build

%install
%make_install


%files
%doc ChangeLog README.md TODO
%license LICENSE
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver
%{_bindir}/xdg-settings
%{_mandir}/man1/xdg-desktop-icon.1*
%{_mandir}/man1/xdg-desktop-menu.1*
%{_mandir}/man1/xdg-email.1*
%{_mandir}/man1/xdg-icon-resource.1*
%{_mandir}/man1/xdg-mime.1*
%{_mandir}/man1/xdg-open.1*
%{_mandir}/man1/xdg-screensaver.1*
%{_mandir}/man1/xdg-settings.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-5
- Prepare for Oreon 11 (RP1)
