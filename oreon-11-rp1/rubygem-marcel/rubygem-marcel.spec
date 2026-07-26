%global source0_hash fdcfcfa33cc52e93c4308d40e4090a5d4ea279e160a7f6af988260fa970e0bee

# Generated from marcel-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name marcel

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 2%{?dist}
Summary: Simple mime type detection using magic numbers, file names, and extensions
# * Portions of Marcel are adapted from the [mimemagic] gem, released under
#   the terms of the MIT License.
# * Marcel's magic signature data is adapted from
#   [Apache Tika](https://tika.apache.org), released under the terms of the
#   Apache License.
License: MIT AND Apache-2.0
URL: https://github.com/rails/marcel
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/marcel.git && cd marcel
# git archive -v -o marcel-1.1.0-test.tar.gz v1.1.0 test/
Source1: %{gem_name}-%{version}-test.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rack)
BuildArch: noarch

%description
Simple mime type detection using magic numbers, file names, and extensions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
ln -s %{builddir}/test .

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/APACHE-LICENSE
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
