# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 25c22b934bc0ae2448f2d73d4b2eba0c59e0521cf5e893fb0b0ad54a461bf066

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gem_name asciidoctor

Name:           rubygem-%{gem_name}
Version:        2.0.26
Release:        1%{?dist}
Summary:        AsciiDoc text processor and publishing toolchain
License:        MIT
URL:            https://asciidoctor.org
Source0:        https://github.com/asciidoctor/asciidoctor/archive/v%{version}/%{gem_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  ruby
BuildRequires:  rubygems-devel

Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       asciidoctor = %{version}-%{release}
Provides:       rubygem(%{gem_name}) = %{version}

%description
A fast, open source text processor and publishing toolchain for converting
AsciiDoc content to HTML 5, DocBook 5, man pages and other formats.

%prep
%oreon_sha256
%autosetup -n %{gem_name}-%{version}

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
cp -p .%{gem_instdir}/man/asciidoctor.1 %{buildroot}%{_mandir}/man1/

%check
instdir=%{buildroot}%{gem_instdir}
run() { ruby -I"$instdir/lib" "$instdir/bin/asciidoctor" "$@"; }

run --version | grep -F '%{version}'

run -o html.out -b html5 README.adoc
grep -q '<html' html.out

run -o docbook.out -b docbook5 README.adoc
grep -q 'docbook.org/ns/docbook' docbook.out

run -o man.out -b manpage man/asciidoctor.adoc
grep -q '^\.TH "ASCIIDOCTOR"' man.out

printf '= Doc\n\nHello *world*.\n' | run -s -o - - | grep -F '<strong>world</strong>'

%files
%license LICENSE
%doc README.adoc CHANGELOG.adoc
%{_bindir}/asciidoctor
%{_mandir}/man1/asciidoctor.1*
%{gem_instdir}
%{gem_cache}
%{gem_spec}
%{gem_docdir}

%changelog
%autochangelog
