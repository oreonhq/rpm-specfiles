%global source2_hash 0fe55175b96a8ea1c4b670cc3fe11d56b341e4eff81b161ea49958ae550be6ca
%global source1_hash 8f875bf880f56276d44389fee54d89a6e6cc3e79f58c011ad31ce7f91a3cc73a
%global source0_hash 0d5f60154382fee10b114a1c34e785d8b1f492073ae2d3a6f7b147687b366aa0
Name:           hello
Version:        2.12.3
Release:        1%{?dist}
Summary:        Prints a familiar, friendly greeting
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://www.gnu.org/software/hello/
Source0:        https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Recommends:     info
Provides:       bundled(gnulib)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
The GNU Hello program produces a familiar, friendly greeting.
Yes, this is another implementation of the classic program that
prints “Hello, world!” when you run it.

However, unlike the minimal version often seen, GNU Hello processes
its argument list to modify its behavior, supports greetings in many
languages, and so on. The primary purpose of GNU Hello is to
demonstrate how to write other programs that do these things; it
serves as a model for GNU coding standards and GNU maintainer
practices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build

%configure
%make_build
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%find_lang hello
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
