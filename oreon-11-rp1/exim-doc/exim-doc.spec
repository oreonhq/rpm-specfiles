%global source0_hash 1d47fd8ffc573bdc9a3ca4b2104dceb2f3e6c6499b67d100a21d7938d6405c50

Summary: Documentation for the exim mail transfer agent
Name: exim-doc
Version: 4.73
Release: 30%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Url: http://www.exim.org/
Source1: ftp://ftp.exim.org/pub/exim/exim4/FAQ-html-20050415.tar.bz2
Source2: ftp://ftp.exim.org/pub/exim/exim4/exim-html-%{version}.tar.bz2
Source3: ftp://ftp.exim.org/pub/exim/exim4/exim-postscript-%{version}.tar.bz2
Source4: ftp://ftp.exim.org/pub/exim/exim4/exim-pdf-%{version}.tar.bz2
Source6: http://www.exim.org/pub/exim/exim4/config.samples-20050415.tar.bz2
BuildArch: noarch

%description
Exim is a mail transport agent (MTA) developed at the University of
Cambridge for use on Unix systems connected to the Internet. This
package contains the documentation for Exim, also available on the 
web at http://www.exim.org/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%setup -q -T -D -a 1
mv FAQ-html faq
%setup -q -T -D -a 2
mkdir html
mv exim-html-*/doc/html html/doc
%setup -q -T -D -a 3
mv exim-postscript-*/ ps
%setup -q -T -D -a 4
mv exim-pdf-*/ pdf
%setup -q -T -D -a 6

find . -name CVS -type d | xargs rm -rf 

%files
%doc faq html ps pdf config.samples

%changelog
%autochangelog
