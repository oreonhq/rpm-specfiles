%global source1_hash 6d9c595d9d052984865a215bb2c2a9c62cdbb8e54253082ae999bb74a724b0a3
%global source0_hash b49f20211fa69fff97d42d6e782a62d7e2da670b064951f14bbff968c93734ae
Name:		unrtf
Summary:        RTF (Rich Text Format) to other formats converter
Version:	0.21.10
Release:        1%{?dist}
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/unrtf
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:	46EA854F5FC5F5A0A9D2BFE89175BF0B3EC83090.gpg
Patch:		0001-Adjust-malloc-types.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
UnRTF is a command-line program written in C which converts documents in
Rich Text Format (.rtf) to HTML, LaTeX, troff macros, and RTF itself.
Converting to HTML, it supports a number of features of Rich Text Format:
    * Changes in the text's font, size, weight (bold), and slant (italic)
    * Underlines and strikethroughs
    * Partial support for text shadowing, outlining, embossing, or engraving
    * Capitalizations
    * Superscripts and subscripts
    * Expanded and condensed text
    * Changes in the foreground and background colors
    * Conversion of special characters to HTML entities

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -ivf
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
