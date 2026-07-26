%global source0_hash 0d5f60154382fee10b114a1c34e785d8b1f492073ae2d3a6f7b147687b366aa0

Name:           hello
Version:        2.12.3
Release:        %autorelease
Summary:        Prints a familiar, friendly greeting
# All code is GPLv3+.
# Parts of the documentation are under GFDL
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://www.gnu.org/software/hello/
Source0:        https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
Recommends:     info
Provides:       bundled(gnulib)

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

%check
make check

%files -f hello.lang
%license COPYING
%{_mandir}/man1/hello.1*
%{_bindir}/hello
%{_infodir}/hello.info*

%changelog
%autochangelog
