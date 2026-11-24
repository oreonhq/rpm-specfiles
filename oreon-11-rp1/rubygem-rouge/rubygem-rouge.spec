# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b77c632842ab7f5147940212f0345808cccfbce864fd5b631d7d12a35ac85452
%global source1_hash e2472b6f55bdf2f5c80db682ac5c582400a78a6e414a5325d02fea1fc82bd321
%global source10_hash 4a510a7d0ba8cd0df97b19854a8fcba3659ea8b5f3de7c8abd5879b7e5bc137c
%global source11_hash 5568b03c72652879f7d07b9bdd27a41fc8d3fc3e2f60ae8b40ff71a2b0f2023f
%global source2_hash 13bf81dccdf5a36c7d1159004e3aeecbae54520faf24a151667e8871e2a21c3c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gem_name rouge

Name:           rubygem-%{gem_name}
Version:        5.1.0
Release:        1%{?dist}
Summary:        Pure-ruby colorizer based on pygments
License:        MIT AND BSD-2-Clause

URL:            http://rouge.jneen.net/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{gem_name}-%{version}-test-missing-files.tar.gz
Source2:        rouge-create-missing-test-files.sh
Source10:       spec_helper_assert.rb
Source11:       bundler.rb
BuildRequires: oreon-rpm-macros
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  help2man
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)

BuildArch:      noarch

%description
Rouge aims to a be a simple, easy-to-extend drop-in replacement for pygments.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source10_hash}  %{SOURCE10}' | sha256sum -c -
echo '%{source11_hash}  %{SOURCE11}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

cp -a %{gem_name}-%{version}/spec .
mkdir FAKE
cp -a %{SOURCE11} FAKE/
cp -pa %{SOURCE10} spec/

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

export GEM_PATH="%{buildroot}%{gem_dir}:%{gem_dir}"

mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -s1 -o %{buildroot}%{_mandir}/man1/rougify.1 \
    %{buildroot}%{_bindir}/rougify

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
    Gemfile \
    %{gem_name}.gemspec \
    %{nil}
popd

%check
find spec -name \*_spec.rb -print0 | \
	grep -v -z "no_building_alternation_pattern_in_regexp_spec" | \
	sort --zero-terminated |  \
	xargs --null ruby -Ilib:FAKE \
	-r./spec/spec_helper \
	-r./spec/spec_helper_assert \
	-r rake/rake_test_loader  \
	%{nil}

%files
%dir %{gem_instdir}

%license %{gem_instdir}/LICENSE

%{gem_libdir}
%exclude %{gem_libdir}/%{gem_name}/demos

%{_bindir}/rougify
%{gem_instdir}/bin
%{_mandir}/man1/rougify.1*

%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_libdir}/%{gem_name}/demos

%changelog
%autochangelog
