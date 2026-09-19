%global source0_hash 4d757cab820cc708b4193cca1df8e333b1d191de5739433131627c1012d8f23a

# Generated from em-websocket-client-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-websocket-client

Name: rubygem-%{gem_name}
Version: 0.1.2
Release: 18%{?dist}
Summary: EventMachine WebSocket Client
License: MIT
URL: http://github.com/mwylde/em-websocket-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(websocket)
BuildRequires: rubygem(eventmachine)
BuildArch: noarch

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
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# %check
# Upstream does not ship tests
# Tested by example on github: https://github.com/mwylde/em-websocket-client/blob/master/README.md#em-websocket-client

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION
%exclude %{gem_instdir}/em-websocket-client.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
%autochangelog
