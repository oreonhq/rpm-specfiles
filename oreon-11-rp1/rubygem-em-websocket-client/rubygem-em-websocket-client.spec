%global source0_hash 4d757cab820cc708b4193cca1df8e333b1d191de5739433131627c1012d8f23a
%global gem_name em-websocket-client
Name: rubygem-%{gem_name}
Version: 0.1.2
Release:        18%{?dist}
Summary:        EventMachine WebSocket Client
License: MIT
URL: http://github.com/mwylde/em-websocket-client
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(eventmachine)
BuildRequires:  rubygem(websocket)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A WebSocket client implementation for EventMachine.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-em-websocket-client-doc -f %{oreon_filedir}/rubygem-em-websocket-client-doc.list

%changelog

%autochangelog
