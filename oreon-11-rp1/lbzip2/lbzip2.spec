%global source0_hash e1772c9a0b76d4146d39bb3408babf9ba06677b88f38bce720aaf1881e10810d
%global commit b6dc48a7b9bfe6b340ed1f6d72133608ad57144b
%global date 20171011
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           lbzip2
Version:        2.5
Release:        1%{?dist}
Summary:        Fast, multi-threaded bzip2 utility
License:        GPL-3.0-or-later
URL:            https://github.com/kjn/lbzip2/
Source0:        https://github.com/kjn/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         lbzip2-gnulib.patch
Patch1: lbzip2-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnulib-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
lbzip2 is an independent, multi-threaded implementation of bzip2. It is
commonly the fastest SMP (and uniprocessor) bzip2 compressor and
decompressor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1

%build

build-aux/autogen.sh
%configure --enable-warnings
%make_build V=1
%install
%make_install
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
