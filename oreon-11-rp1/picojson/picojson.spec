# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 671f89832a17e9e71398f80c0a326afa2ebe81f4c26d5a9992e1fcd0888ae151
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global commit  111c9be5188f7350c2eac9ddaedd8cca3d7bf394
%global date    20210117

Name:           picojson
Summary:        A header-file-only, JSON parser / serializer in C++
Version:        1.3.0

Release:        %{autorelease}
License:        BSD-2-Clause
URL:            https://github.com/kazuho/picojson
Source0:        https://github.com/kazuho/picojson/archive/%{commit}/picojson-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc-c++
BuildRequires:  make

%global desc %{expand:
PicoJSON is a tiny JSON parser / serializer for C++ with following properties:
Header-file only, No external dependencies (only uses standard C++ libraries),
STL-friendly (arrays are represented by using std::vector, objects are std::map)
provides both pull interface and streaming (event-based) interface.}

%description
%desc

%package devel
Summary:        Header files for picojson development
Provides:       %{name}-static = %{version}-%{release}

%description devel
%desc

%prep
%oreon_sha256
%autosetup -n picojson-%{commit}

%build

%check
%make_build test

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 0644 picojson.h %{buildroot}%{_includedir}/picojson.h

%files devel
%{_includedir}/picojson.h
%doc README.mkdn examples
%license LICENSE

%changelog
%autochangelog
