%global source0_hash c677885a51bac44551b0ddeb4078f456e7d06a971a0f3fbdc701c1a2eb9b5975
%global git_rev_full 63ec47c5e295ad4f09d1df6d92afb7e10c3fec39
%global git_rev %(c=%{git_rev_full}; echo ${c:0:6})
%global git_date 20150213
Name:		obconf
Version:	2.0.4
Release:        1%{?dist}
Summary:        A graphical configuration editor for the Openbox window manager
License:	GPL-2.0-or-later
URL:		http://icculus.org/openbox/index.php/ObConf:About
Source0:        https://github.com/danakj/%{name}/archive/%{git_rev}/%{name}-%{git_rev}.tar.gz
Patch0: obconf-c99.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openbox-devel
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel
# /oreon:deps
%description
ObConf is a graphical configuration editor for the Openbox window manager. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_rev_full}

%build

./bootstrap
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications	\
	--add-category	X-Fedora	\
	--delete-original	\
	%{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
