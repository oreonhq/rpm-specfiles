%global source0_hash af6e7186c483e101725703f32d28f77d31a0a770c9a81f6e41a880fd3dc25dec

# Generated from rack-session-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rack-session

Name: rubygem-%{gem_name}
Version: 2.1.1
Release: 4%{?dist}
Summary: A session implementation for Rack
License: MIT
URL: https://github.com/rack/rack-session
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatibility with minitest 6
Patch0:  rack-session-2.1.1-minitest6.patch
# git clone https://github.com/rack/rack-session.git && cd rack-session
# git archive -v -o rack-session-2.1.1-tests.tar.gz v2.1.1 test/
Source1: rack-session-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5
BuildRequires: rubygem(base64)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-global_expectations)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(rack)
BuildArch: noarch

%description
A session implementation for Rack.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
( cd %{builddir}/test
%patch -P0 -p2
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

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

ruby -Itest -e 'Dir.glob "./test/**/spec_*.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%{gem_libdir}
%license %{gem_instdir}/license.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/readme.md
%doc %{gem_instdir}/releases.md
%doc %{gem_instdir}/security.md

%changelog
%autochangelog
