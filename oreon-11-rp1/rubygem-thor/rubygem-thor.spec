%global source1_hash 08fb714bef57b8a4b9a91862cee79fbb8a3e6f2548a86430394702fdba00acbb
%global source0_hash eef0293b9e24158ccad7ab383ae83534b7ad4ed99c09f96f1a6b036550abbeda
%global gem_name thor
Name: rubygem-%{gem_name}
Version: 1.3.2
Release:        1%{?dist}
Summary:        Thor is a toolkit for building powerful command-line interfaces
License: MIT
URL: http://whatisthor.com/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/thor/archive/refs/tags/v1.3.2.tar.gz
Patch0: rubygem-thor-1.3.2-Support-Ruby-3-4-Hash-inspect-change.patch
Recommends: rubygem(io-console)
BuildArch: noarch
# oreon:deps
BuildRequires:  //bin/git
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(readline)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

( cd %{builddir}
%patch 0 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/spec .
sed -i '/simplecov/,/end/ s/^/#/' spec/helper.rb
rspec spec
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-thor-doc -f %{oreon_filedir}/rubygem-thor-doc.list

%changelog

%autochangelog
