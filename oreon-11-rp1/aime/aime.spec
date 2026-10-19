%global source0_hash 1d2f1c987830e356eabdf67825909855cd0aa2ce453d29aac7cdbc5931542fd1
%global libname libaime
Name:            aime
Version:         8.20250217
Release:        1%{?dist}
Summary:        An application embeddable programming language interpreter
License:         GPL-3.0-or-later
URL:             http://aime-embedded.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/aime-embedded/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:          %{name}-8.20150211-ldflags.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
aime is a programming language with a C like syntax, intended for application
extending purposes. The aime collection comprises the language description, an
application embeddable interpreter (libaime), the interpreter C interface
description and a standalone interpreter. Many examples on how the interpreter
can be used (embedded in an application) are also available, together with 
some hopefully useful applications, such as expression evaluators.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     devel
This package contains header files for developing applications that 
use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags CFLAGS="%{optflags} -std=gnu17"
%configure CFLAGS="$CFLAGS"
%make_build
%check

make check
%install
%make_install
find %{buildroot} -name '*.a' -delete -print
rm -frv %{buildroot}%{_infodir}/dir
%oreon_autofiles aime-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n aime-devel -f %{oreon_filedir}/aime-devel.list

%changelog

%autochangelog
