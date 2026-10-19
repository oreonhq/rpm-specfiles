%global source0_hash 1562d866060ae275fa1d9c449a34928e79976df688339171ea35b9519d81ac1a
%define    svn_date 20080213
Name:           ksig
Version:        1.1
Release:        1%{?dist}
Summary:        A graphical application to manage multiple email signatures
License:        GPL-2.0-or-later
URL:            http://extragear.kde.org
Source0:        %{name}-%{version}-svn.tar.bz2
Patch0:         ksig-1.1-svn-cmakelists.patch
Patch1:         ksig-1.1-svn-docsdir.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  kde-filesystem
BuildRequires:  kdelibs4-devel
BuildRequires:  libutempter-devel
BuildRequires:  make
# /oreon:deps
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
desktop-file-install --vendor ""                          \
        --dir %{buildroot}%{_datadir}/applications/kde4   \
        %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
