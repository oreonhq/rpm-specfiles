%global source0_hash d41d7dc3eecde6e4339bebdcc731ab9f88a486fe57d7606a48f917c19b0739c6

%global gitver 26b1454a
%global date   20130626

Summary:       Visual tool for Git
Name:          teamgit
Version:       0.0.12
Release:       42.%{date}%{?dist}
Epoch:         1
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           http://gitorious.org/projects/teamgit
# Source0:     http://ppa.launchpad.net/bain-devslashzero/ubuntu/pool/main/t/teamgit/teamgit_0.0.10ubuntu1.tar.gz
# Tarball created by
# $ git clone git://gitorious.org/teamgit/mainline.git
# $ cd mainline
# $ git checkout origin/master
# $ git archive --format=tar --prefix=teamgit-%{version}/ %{gitver} | xz > teamgit-%{version}-%{date}.tar.xz
Source0:       teamgit-%{version}-%{date}.tar.xz
Patch01:       teamgit-0.0.12.format.patch
BuildRequires: make
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: source-highlight-qt-devel
BuildRequires: qt-devel
Requires:      git
%description
This package provides a visual tool for Git, a distributed revision
control system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%{qmake_qt4} ./teamgit.pro
make
#{?_smp_mflags} don't work

%install
make INSTALL_ROOT=%{buildroot} install
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop 

%files
%doc COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-rebase
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_icon.png
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
