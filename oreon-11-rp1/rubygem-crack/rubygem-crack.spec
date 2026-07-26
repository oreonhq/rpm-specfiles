%global source0_hash ff4a10390cd31d66440b7524eb1841874db86201d5b70032028553130b6d4c7e

%global gem_name crack

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 2%{?dist}
Summary: Really simple JSON and XML parsing, ripped from Merb and Rails
License: MIT
URL: https://github.com/jnunemaker/crack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/jnunemaker/crack.git && cd crack
# git archive -v -o crack-1.0.1-tests.tar.gz v1.0.1 test/
Source1: crack-%{version}-tests.tar.gz
BuildRequires: rubygems-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rexml)
BuildArch: noarch
#BZ 781829
Epoch: 1

%description
Really simple JSON and XML parsing, ripped from Merb and Rails.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
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
ln -s %{builddir}/test test

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
