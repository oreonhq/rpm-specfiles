%global source0_hash b7e7a74e2410b5e85c25858b26b3322f29161e300935f70a0e0d3c35e0462737

# Generated from websocket-1.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name websocket

Name: rubygem-%{gem_name}
Version: 1.2.11
Release: 4%{?dist}
Summary: Universal Ruby library to handle WebSocket protocol
License: MIT
URL: http://github.com/imanel/websocket-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby 
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webrick)
BuildArch: noarch

%description
Universal Ruby library to handle WebSocket protocol.

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
rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/websocket.gemspec

%changelog
%autochangelog
