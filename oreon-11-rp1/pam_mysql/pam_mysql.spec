%global source0_hash 83274d708829568703a942d83460a07a597410668f2bbeb3650184f81593dd6e

Summary:       PAM module for auth UNIX users using MySQL data base
Name:          pam_mysql
Version:       1.0.0~beta1
Release:       13%{?dist}
Epoch:         1
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
Source0:       https://github.com/NigelCunningham/pam-MySQL/archive/refs/tags/1.0.0-beta1.tar.gz
# https://github.com/NigelCunningham/pam-MySQL/issues/80
Patch:         0001-Remove-hard-coded-install_dir-and-use-libdir-instead.patch
# https://github.com/NigelCunningham/pam-MySQL/pull/81
Patch:         0002-Remove-name-prefix-to-shared-library-is-named-pam_my.patch
URL:           https://github.com/NigelCunningham/pam-MySQL
BuildRequires: meson gcc
BuildRequires: mariadb-connector-c-devel pam-devel
BuildRequires: libxcrypt-devel
Requires:      pam

%description
Pam_mysql aims to provide a backend neutral means of authenticating
users against an MySQL database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pam-MySQL-1.0.0-beta1

%build
%meson
%meson_build

mv AUTHORS AUTHORS.lame
iconv -f latin1 -t utf-8 -o AUTHORS AUTHORS.lame

%install
%meson_install

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/security/pam_mysql.so

%changelog
%autochangelog
