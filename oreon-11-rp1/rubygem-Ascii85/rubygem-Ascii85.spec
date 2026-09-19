%global source0_hash 87936ae8372b971aeed2dbdaa4d25c70fe098517d2a506fa4a076dc38919738a

%global gem_name Ascii85

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 12%{?dist}
Summary: Ascii85 encoder/decoder
License: MIT
URL: https://github.com/DataWraith/ascii85gem/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
#retrieved from http://rubyforge.org/tracker/index.php?func=detail&aid=29377&group_id=7826&atid=30313
Source1: ascii85.1.pod.tgz 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: %{_bindir}/pod2man
BuildArch: noarch

%description
Ascii85 provides methods to encode/decode Adobe's binary-to-text encoding of
the same name.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

pod2man --center "" --release "" --name ASCII85 --utf8 --section=1 ../ascii85.1.pod ../ascii85.1

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

mv %{buildroot}%{gem_instdir}/{History.txt,README.md} ./
rm -rf %{buildroot}%{gem_instdir}/.travis.yml

install -D -m 644 ../ascii85.1 %{buildroot}%{_mandir}/man1/ascii85.1

sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' %{buildroot}%{gem_instdir}/bin/ascii85

%check
pushd .%{gem_instdir}
ruby -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/ascii85
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/ascii85.1*

%files doc
%doc History.txt README.md
%doc %{gem_docdir}
%{gem_instdir}/Ascii85.gemspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
%autochangelog
