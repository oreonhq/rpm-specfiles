%global source0_hash 4ee5cb30341627a1d5d928e02353dd69e8c00e8a6301815762e253ce3a9e84af
%global gem_name stomp
Summary:        Ruby client for the Stomp messaging protocol
Name: rubygem-%{gem_name}
Version: 1.4.10
Release:        1%{?dist}
License: Apache-2.0
URL: https://github.com/stompgem/stomp
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: https://salsa.debian.org/ruby-team/ruby-stomp/-/raw/5be6383a7a34a1d1891708d6aa8688cb4a6f89a5/debian/patches/fix-FTBFS-with-ruby-rspec-3.12.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby client for the Stomp messaging protocol

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
%description doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P 0 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{buildroot}/%{gem_instdir}
rspec  -Ilib spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-stomp-doc -f %{oreon_filedir}/rubygem-stomp-doc.list

%changelog

%autochangelog
