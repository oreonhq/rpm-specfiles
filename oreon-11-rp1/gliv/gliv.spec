%global source0_hash 5be6d071927dcb371676a9e4e9e4c54e8b2f4842f04dd63727b9a5032ddbcb69
Summary:        Image viewing utility
Name:		gliv
Version:	1.9.7
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		http://guichaz.free.fr/gliv/
VCS:		git://repo.or.cz/gliv.git
Source0:        http://guichaz.free.fr/gliv/files/%{name}-%{version}.tar.bz2
Source1:	gliv.desktop
Source2:	gliv.applications
Patch1:		gliv-0001-Something-is-always-bigger-than-nothing-NULL.patch
Patch2:		gliv-0002-bool-is-a-reserved-word-in-a-new-ANSI-C.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  make
# /oreon:deps
%description
GLiv is an OpenGL image viewer. GLiv is very fast and smooth at rotating,
panning and zooming if you have an OpenGL accelerated graphics board.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%find_lang %{name}
install -D -p -m 0644 %{SOURCE2}  %{buildroot}%{_datadir}/application-registry/gliv.applications
install -D -p -m 0644 gliv.png %{buildroot}%{_datadir}/pixmaps/gliv.png
install -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
