%global source0_hash 686ad5a0ecdfca67a3a09593a2507a7825258fbf1561238b4917f61d9e50ad91

# Generated from globalid-0.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name globalid

%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 6%{?dist}
Summary: Refer to any model with a URI: gid://app/class/id
License: MIT
URL: http://www.rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/globalid.git && cd globalid
# git archive -v -o globalid-1.2.1-tests.tar.gz v1.2.1 test
Source1: %{gem_name}-%{version}-tests.tar.gz
# Fix Ruby 3.4 compatibility.
# https://github.com/rails/globalid/pull/192
Patch0: rubygem-globalid-1.2.1-Keep-using-URI-RFC2396-parser.patch
# Fix Rails 8 compatibility.
# https://github.com/rails/globalid/pull/197/commits/f05f178f6960e85f6cdb6d6bf8c1812fd83af74a
Patch1: rubygem-globalid-1.2.1-Fix-cache-format-for-Rails-8.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
%if %{without bootstrap}
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(activemodel)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(railties)
%endif
BuildArch: noarch

%description
URIs for your models makes it easy to pass references around.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%patch 0 -p1

( cd %{builddir}
%patch 1 -p1
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# Avoid Bundler dependency.
sed -i "/bundler\/setup/ s/^/#/" ./test/helper.rb

# Prevent `NameError: uninitialized constant ActionController::Base` by
# explicit `-raction_controller`.
# https://github.com/rails/rails/issues/55215
ruby -Ilib:test -raction_controller -e "Dir.glob './test/cases/*test.rb', &method(:require)"
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
