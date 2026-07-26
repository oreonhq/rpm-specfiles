%global source0_hash 8b78bf29715df1e3b2498d8daadcc71b8df0ebae3b031581b2b290bd143e84c6

%global realname mimetypes

Name:		erlang-%{realname}
Version:	1.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang MIME types library
License:	BSD-3-Clause
URL:		https://github.com/erlangpack/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-mimetypes-0001-Update-mime.types.patch
Patch2:		erlang-mimetypes-0002-Use-NL-value-in-COMMENT-declaration.patch
Patch3:		erlang-mimetypes-0003-Skip-MIME-types-w-o-extension.patch
Patch4:		erlang-mimetypes-0004-Unknow-extension-returns-application-octet-stream.patch
Patch5:		erlang-mimetypes-0005-Parse-empty-strings-properly.patch
Patch6:		erlang-mimetypes-0006-No-unicode-symbols-in-file-extensions-allowed.patch
BuildRequires:	erlang-proper
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
install -D -p -m 0644 priv/mime.types %{buildroot}%{erlang_appdir}/priv/mime.types

%check
%{erlang3_test}

%files
%doc README.md THANKS
%{erlang_appdir}/

%changelog
%autochangelog
