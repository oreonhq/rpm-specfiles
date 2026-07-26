%global source0_hash 8d924d75ea9ccf9cfffb10f1396c482b4878846d054d3d62c6dd0d55549be9bb

# Generated from thor-0.12.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name thor

Name: rubygem-%{gem_name}
Version: 1.3.2
Release: 4%{?dist}
Summary: Thor is a toolkit for building powerful command-line interfaces
License: MIT
URL: http://whatisthor.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The test suite is not shipped with the gem, you may check it out like so:
# git clone https://github.com/rails/thor.git --no-checkout
# cd thor && git archive -v -o thor-1.3.2-spec.tar.gz v1.3.2 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# Support Ruby 3.4 Hash#inspect change.
# https://github.com/rails/thor/commit/9d7aef1db1666ecc382eeaa5549361a0aa956567
Patch0: rubygem-thor-1.3.2-Support-Ruby-3-4-Hash-inspect-change.patch
# Thor lazy loads rubygem(io-console).
Recommends: rubygem(io-console)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rake)
BuildRequires: rubygem(readline)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: %{_bindir}/git
BuildArch: noarch

%description
Thor is a toolkit for building powerful command-line interfaces.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

( cd %{builddir}
%patch 0 -p1
)

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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'

%check
( cd .%{gem_instdir}
cp -a %{builddir}/spec .

# kill simplecov dependency
sed -i '/simplecov/,/end/ s/^/#/' spec/helper.rb

rspec spec
)

%files
%dir %{gem_instdir}
%{_bindir}/thor
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/.document
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/thor.gemspec

%changelog
%autochangelog
