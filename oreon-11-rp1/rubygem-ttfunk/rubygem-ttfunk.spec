%global source0_hash 2370ba484b1891c70bdcafd3448cfd82a32dd794802d81d720a64c15d3ef2a96
%global gem_name ttfunk
Summary:        Font Metrics Parser for Prawn
Name: rubygem-%{gem_name}
Version: 1.7.0
Release:        14%{?dist}
License: GPL-2.0-only OR GPL-3.0-only OR Ruby
URL: https://github.com/prawnpdf/ttfunk
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-spec.txz
Requires: rubygem(bigdecimal)
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems
BuildRequires:  rubygems-devel
# /oreon:deps
%description
TTFunk is a TrueType font parser written in pure ruby.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}
%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
rm -rf ./%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc
%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec .
rspec spec
popd
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-ttfunk-doc -f %{oreon_filedir}/rubygem-ttfunk-doc.list

%changelog

%autochangelog
