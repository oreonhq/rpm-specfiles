%global source2_hash 3f896ba81227db908bc631b9084f2307262bc3800e5ac747e4ffd6d492cfef07
%global source1_hash 897d6d58d67847d116d8461e95ea6ae632f06da36c6d4c5a6715a1fc77882af6
%global source0_hash 0661e531e4c0ef097959aa1c9773796585db39c72c84a02ff87d2c3637c620cb
Summary:        Tool to search text in PDF files
Name:           pdfgrep
Version:        2.2.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://pdfgrep.org/
Source0:        https://pdfgrep.org/download/%{name}-%{version}.tar.gz
Source1:        https://pdfgrep.org/download/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/432FC753112F26D9EB48DDC1A17CF2CA697BEAF2
Patch:          pdfgrep-2.2.0-disallow-ligatures.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  poppler-cpp-devel
# /oreon:deps
%description
Pdfgrep is a tool, that works similar to grep, to search text in PDF files.
It tries to be compatible with GNU grep, thus many of the favorite GNU grep
options are supported. Pdfgrep can search many PDFs at once, even recursively
in directories. It supports regular expressions (POSIX and PCRE), provides
colored output and finally also support for password protected PDF files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
