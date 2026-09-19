%global source0_hash 44d76ef0eb76bf3f443a86b2fc80106f54cd8c001bafb354429e2a005c5eb415

%global gem_name rr

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 12%{?dist}
Summary: RR is a test double framework with a terse syntax
License: MIT
URL: https://rr.github.io/rr
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rr/rr.git && cd rr
# git checkout v1.2.1 && tar czvf rr-1.2.1-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# The following are for running test suite
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(test-unit-rr)
BuildRequires: rubygem(ostruct)
BuildArch: noarch

%description
RR is a test double framework that features a rich selection of double
techniques and a terse syntax.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}

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
pushd .%{gem_instdir}
tar xvzf %{SOURCE1}
ruby test/run-test.rb
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Appraisals
%{gem_instdir}/CHANGES.md
%{gem_instdir}/CREDITS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/gemfiles
%{gem_instdir}/rr.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
