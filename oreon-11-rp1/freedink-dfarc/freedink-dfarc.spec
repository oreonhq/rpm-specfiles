%global source0_hash a51124ecd11eeca0f1d16732ef58ee690e2fa2db06cc0ec2a5b61b41f8b0e8fa
Name:		freedink-dfarc
Version:	3.14
Release:        1%{?dist}
Summary:        Frontend and .dmod installer for GNU FreeDink
License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/freedink/
Source0:        https://ftp.gnu.org/gnu/freedink/dfarc-%{version}.tar.gz
ExcludeArch:    s390x
%if 0%{?suse_version}
%else
%endif
Requires:	xdg-utils
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
DFArc makes it easy to play and manage the Dink Smallwood game and
it's numerous Dink Modules (or D-Mods).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dfarc-%{version}

%build

%configure --disable-desktopfiles
%make_build
%install
%make_install
%find_lang dfarc
desktop-file-validate %{buildroot}/%{_datadir}/applications/%name.desktop
%if 0%{?suse_version}
%suse_update_desktop_file -i %name
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
