%global source0_hash 0c7c3d66aed00133f3889bb449d38c745fb2c757a302c067ace2b65981259422
Name:           undbx
Version:        0.21
Release:        1%{?dist}
Summary:        Outlook Express .dbx files extractor
License:        GPL-3.0-or-later
URL:            https://github.com/ZungBang/undbx
Source0:        https://github.com/ZungBang/undbx/archive/undbx-%{version}.tar.gz
Patch0:         0001-Adjust-strncpy-call-to-not-use-string-length.patch
%define _pkg_extra_cflags -Wno-error=unused-but-set-variable
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
UnDBX is a tool to extract, recover and undelete e-mail messages from 
Outlook Express .dbx file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
