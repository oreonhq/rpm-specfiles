%global source0_hash f97293c8a3343db6765ff58811c13143944c3cb22e001830248fed8adbc1c7b7
%global gem_name cucumber-gherkin
Name: rubygem-%{gem_name}
Version: 22.0.0
Release:        1%{?dist}
Summary:        Fast Gherkin lexer/parser
License: MIT
URL: https://github.com/cucumber/gherkin
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{name}-%{version}-testdata.txz
Patch0: rubygem-cucumber-gherkin-29.0.0-Fix-compatibility-with-cucumber-messages-25.patch
BuildArch: noarch
Provides: rubygem-gherkin = %{version}-%{release}
Obsoletes: rubygem-gherkin < 5.1.0-100
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(cucumber-messages)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%patch 0 -p2

%gemspec_remove_dep -g cucumber-messages "~> 17.1", ">= 17.1.1"
%gemspec_add_dep -g cucumber-messages ">= 17.0"

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/testdata testdata
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-cucumber-gherkin-doc -f %{oreon_filedir}/rubygem-cucumber-gherkin-doc.list

%changelog

%autochangelog
