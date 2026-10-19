%global source0_hash b7e7a74e2410b5e85c25858b26b3322f29161e300935f70a0e0d3c35e0462737
%global gem_name websocket
Name: rubygem-%{gem_name}
Version: 1.2.11
Release:        4%{?dist}
Summary:        Universal Ruby library to handle WebSocket protocol
License: MIT
URL: http://github.com/imanel/websocket-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-websocket-doc -f %{oreon_filedir}/rubygem-websocket-doc.list

%changelog

%autochangelog
