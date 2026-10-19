%global source0_hash fff9880d5dc35950e7706cf132fd297f377c049101794be1cf01c95567f642d4
%global gem_name typhoeus
Name: rubygem-%{gem_name}
Version: 1.4.0
Release:        16%{?dist}
Summary:        Parallel HTTP library on top of libcurl multi
License: MIT
URL: https://github.com/typhoeus/typhoeus
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: typhoeus-1.4.0-Fix-Ruby-3-0-compatibility.patch
Patch1: typhoeus-1.4.0-support-curl-8_9-msg.patch
Patch2: rubygem-typhoeus-1.4.1-Fix-Rack-3-compatibility.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/rackup
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(dalli)
BuildRequires:  rubygem(ethon)
BuildRequires:  rubygem(faraday)
BuildRequires:  rubygem(redis)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(sinatra)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Like a modern code version of the mythical beast with 100 serpent heads,
Typhoeus runs HTTP requests in parallel while cleanly encapsulating handling
logic.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
sed -i -e '/^#!/d' %{buildroot}%{gem_instdir}/spec/support/server.rb
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i -e '/[bB]undler/ s/^/#/' spec/spec_helper.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-typhoeus-doc -f %{oreon_filedir}/rubygem-typhoeus-doc.list

%changelog

%autochangelog
