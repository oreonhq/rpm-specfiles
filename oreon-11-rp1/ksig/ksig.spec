%global source0_hash 1562d866060ae275fa1d9c449a34928e79976df688339171ea35b9519d81ac1a

# Review request:
# https://bugzilla.redhat.com/show_bug.cgi?id=432701

%define    svn_date 20080213

Name:           ksig
Version:        1.1
Release:        0.41.%{svn_date}%{?dist}
Summary:        A graphical application to manage multiple email signatures

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://extragear.kde.org

# Creation of tarball from svn
#
# Kevin Kofler enhanced the create_tarball.rb script from upstream to also support ksig
# This script also download the translations and docs
# To use it you will need the script itself and a config.ini in the same directory
#
# http://repo.calcforge.org/f9/kde4-tarballs/create_tarball.rb
# http://repo.calcforge.org/f9/kde4-tarballs/config.ini
#
# To create a new checkout use it with anonymous svn access
# ./create_tarball.rb -n
# At the prompt you have to enter "ksig" (without brackets)

Source0:        %{name}-%{version}-svn.tar.bz2
# fix CMakeLists.txt so this builds as a standalone directory (without all of extragear-pim)
Patch0:         ksig-1.1-svn-cmakelists.patch
# Install documentation into the correct subdir
Patch1:         ksig-1.1-svn-docsdir.patch

BuildRequires:  kdelibs4-devel
BuildRequires:  kde-filesystem >= 4
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  libutempter-devel
BuildRequires: make

%description
KSig is a graphical tool for keeping track of many different email signatures.
The signatures themselves can be edited through KSig's graphical user 
interface. A command-line interface is then available for generating random 
or daily signatures from a list. The command-line interface makes a suitable 
plugin for generating signatures in external mail clients such as KMail.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}-svn
%patch -P0 -p1 -b .cmakelists
%patch -P1 -p1 -b .docsdir

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# validate desktop file
desktop-file-install --vendor ""                          \
        --dir %{buildroot}%{_datadir}/applications/kde4   \
        %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.DOC
%{_docdir}/HTML/en/ksig/
%{_kde4_bindir}/ksig
%{_kde4_appsdir}/ksig/
%{_kde4_iconsdir}/hicolor/*/apps/ksig.png
%{_datadir}/applications/kde4/ksig.desktop

%changelog
%autochangelog
