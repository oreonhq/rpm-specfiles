%global source0_hash d29b0b9890eed965f8b84ce139579a87b960dc8de22a7fbba236d90c7f0b9a59

Name:           undbx
Version:        0.21
Release:        %autorelease
Summary:        Outlook Express .dbx files extractor
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/ZungBang/undbx
Source0:        https://github.com/ZungBang/undbx/archive/undbx-%{version}.tar.gz

# https://github.com/ZungBang/undbx/pull/3
Patch0:         0001-Adjust-strncpy-call-to-not-use-string-length.patch

BuildRequires: make
BuildRequires:  gcc

%define _pkg_extra_cflags -Wno-error=unused-but-set-variable

%description
UnDBX is a tool to extract, recover and undelete e-mail messages from 
Outlook Express .dbx file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc README.rst
%license COPYING
%{_bindir}/undbx
%exclude %{_bindir}/undbx.hta

%changelog
%autochangelog
