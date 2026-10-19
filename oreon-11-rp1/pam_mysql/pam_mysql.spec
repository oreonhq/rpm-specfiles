%global source0_hash 83274d708829568703a942d83460a07a597410668f2bbeb3650184f81593dd6e
Summary:        PAM module for auth UNIX users using MySQL data base
Name:          pam_mysql
Version:       1.0.0~beta1
Release:        13%{?dist}
Epoch:         1
License:       GPL-2.0-or-later
Source0:        https://github.com/NigelCunningham/pam-MySQL/archive/refs/tags/1.0.0-beta1.tar.gz
Patch:         0001-Remove-hard-coded-install_dir-and-use-libdir-instead.patch
Patch:         0002-Remove-name-prefix-to-shared-library-is-named-pam_my.patch
URL:           https://github.com/NigelCunningham/pam-MySQL
Requires:      pam
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  meson
BuildRequires:  pam-devel
# /oreon:deps
%description
Pam_mysql aims to provide a backend neutral means of authenticating
users against an MySQL database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pam-MySQL-1.0.0-beta1
%oreon_prep
%build

%meson
%meson_build
mv AUTHORS AUTHORS.lame
iconv -f latin1 -t utf-8 -o AUTHORS AUTHORS.lame
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
