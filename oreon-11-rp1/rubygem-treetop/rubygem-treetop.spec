%global source1_hash 190b5f5fa5e77b862f201d72659be33d715ad8d99c146355a0a32b2b75774dc5
%global source0_hash ed48add684a2d7a8fd6e3b8b027d8ee5983b50977ae691913131a24f1746ac29
%global gem_name treetop
Name: rubygem-%{gem_name}
Version: 1.6.12
Release:        1%{?dist}
Summary:        A Ruby-based text parsing and interpretation DSL
License: MIT
URL: https://github.com/cjheath/treetop
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/cjheath/treetop/archive/refs/tags/v1.6.12.tar.gz
Patch0:  treetop-gh61-IO_popen-ruby40.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(polyglot)
BuildRequires:  rubygem(rr)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A Parsing Expression Grammar (PEG) Parser generator DSL for Ruby.

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
(
cd %{_builddir}
%patch -P0 -p1
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
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/doc/tt.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-treetop-doc -f %{oreon_filedir}/rubygem-treetop-doc.list

%changelog

%autochangelog
