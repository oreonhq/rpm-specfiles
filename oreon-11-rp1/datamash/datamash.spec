%global source0_hash f382ebda03650dd679161f758f9c0a6cc9293213438d4a77a8eda325aacb87d2
Name:           datamash
Version:        1.9
Release:        1%{?dist}
Summary:        A statistical, numerical and textual operations tool
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/%{name}/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(lib)
BuildRequires:  pkgconfig
BuildRequires:  texinfo
# /oreon:deps
%description
GNU datamash is a command-line program which performs basic
numeric,textual and statistical operations on input textual data
files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%{__rm} -f %{buildroot}/%{_infodir}/dir
%find_lang %{name}
%{__mkdir_p} %{buildroot}%{bash_completions_dir}
%{__mv} %{buildroot}%{_datadir}/datamash/bash-completion.d/datamash %{buildroot}%{bash_completions_dir}
%{__sed} -i '/^#!/,1d' %{buildroot}%{bash_completions_dir}/datamash
%oreon_autofiles main

%check

%{__make} check || { echo 'begin test-suite.log'; cat test-suite.log; echo 'end test-suite.log'; false; }
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
