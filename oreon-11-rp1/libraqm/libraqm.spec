# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4d76a358358d67c5945684f2f10b3b08fb80e924371bf3ebf8b15cd2e321d05d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:				libraqm
Version:			0.10.1
Release:			1%{?dist}
License:			MIT
Summary:			Complex Textlayout Library
Summary(ar):		مكتبة رقم للنّصوص المركّبة
URL:				https://github.com/HOST-Oman/libraqm
Source0:        %{url}/releases/download/v%{version}/raqm-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:		meson
BuildRequires:		freetype-devel
BuildRequires:		harfbuzz-devel
BuildRequires:		fribidi-devel
BuildRequires:		gtk-doc

%package docs
Summary:			Libraqm Documentation
Summary(ar):		وثائق مكتبة رقم
BuildArch:			noarch

%package devel
Summary:			Complex Textlayout Library
Summary(ar):		مكتبة رقم للنّصوص المركّبة
Requires:			libraqm%{?_isa} = %{version}-%{release}

%description
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%description -l ar
مكتبة تستخدم لتأطير النًصوص المركّبة، مقدمة
مدخلًا برمجيًا مريحًا.

%description devel
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%description -l ar devel
مكتبة تستخدم لتأطير النًصوص المركّبة، مقدمة
مدخلًا برمجيًا مريحًا.

%description docs
This package contains documentation files for raqm.

%description -l ar docs
وثائق مكتبة رقم.

%prep
%oreon_sha256
%autosetup -p1 -n raqm-%{version}

%build
%meson -Ddocs=true
%meson_build

%check
export LC_ALL=C.utf8
%meson_test

%install
%meson_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

%files
%license COPYING
%{_libdir}/libraqm.so.*

%files devel
%license COPYING
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc

%files docs
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/gtk-doc/html/raqm

%changelog
%autochangelog
