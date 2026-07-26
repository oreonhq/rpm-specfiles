%global source0_hash 655479603bdc5f4345f2bc2735b901690da668a46984bd3839c73309d0847eab

# Generated from websocket-extensions-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name websocket-extensions

Name: rubygem-%{gem_name}
Version: 0.1.5
Release: 8%{?dist}
Summary: Generic extension manager for WebSocket connections
License: Apache-2.0
URL: https://github.com/faye/websocket-extensions-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/faye/websocket-extensions-ruby.git && \
#   cd websocket-extensions-ruby \
#   git archive -v -o websocket-extensions-0.1.5-specs.tar.gz 0.1.5 spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
# Fix RSpec 3.10.3+ compatibility.
# https://github.com/faye/websocket-extensions-ruby/commit/5891358639fcfa7a2e2004855275bd7da0c85c64
Patch0: rubygem-websocket-extensions-0.1.5-Use-explicit-has-to-avoid-confusion-with-keyword-args.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Generic extension manager for WebSocket connections.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch -P0 -p1
popd

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
cp -a %{_builddir}/spec spec
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
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
