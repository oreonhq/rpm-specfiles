%global source0_hash 00d620939c710788ae3f71188ef913e0aa7ff0a5a39f48249213ea6215558c8d

# Generated from jekyll-email-protect-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jekyll-email-protect

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 16%{?dist}
Summary: A simple liquid filter which converts emails into percent-encoded strings
License: MIT
URL: https://github.com/vwochnik/jekyll-email-protect
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: %{_bindir}/rspec
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem(liquid)
BuildArch: noarch

%description
Email protection liquid filter for Jekyll.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

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

# We do not need whole jekyll, using just liquid is sufficient.
# https://github.com/vwochnik/jekyll-email-protect/pull/8
sed -i "/require 'jekyll'/ s/'jekyll'/'liquid'/" spec/spec_helper.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
%autochangelog
