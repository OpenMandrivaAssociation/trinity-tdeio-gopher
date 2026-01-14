%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tdeio-gopher
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.1.4
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	tdeio-slave for the gopher protocol
Group:		Productivity/Networking/Ftp/Clients
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/tdeio/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Adds support for the "gopher:" protocol
to Konqueror and other TDE applications.

This enables you to perform gopher searches in Konqueror.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang tdeio_gopher


%files -f tdeio_gopher.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING FAQ README VERSION
%{tde_prefix}/%{_lib}/trinity/tdeio_gopher.la
%{tde_prefix}/%{_lib}/trinity/tdeio_gopher.so
%{tde_prefix}/share/services/gopher.protocol
%lang(ca) %{tde_prefix}/share/doc/tde/HTML/ca/tdeioslave/
%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/tdeioslave/
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/tdeioslave/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/
%lang(en_GB) %{tde_prefix}/share/doc/tde/HTML/en_GB/tdeioslave/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/tdeioslave/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/tdeioslave/
%lang(fr) %{tde_prefix}/share/doc/tde/HTML/fr/tdeioslave/
%lang(gl) %{tde_prefix}/share/doc/tde/HTML/gl/tdeioslave/
%lang(hu) %{tde_prefix}/share/doc/tde/HTML/hu/tdeioslave/
%lang(it) %{tde_prefix}/share/doc/tde/HTML/it/tdeioslave/
%lang(nl) %{tde_prefix}/share/doc/tde/HTML/nl/tdeioslave/
%lang(pl) %{tde_prefix}/share/doc/tde/HTML/pl/tdeioslave/
%lang(pt) %{tde_prefix}/share/doc/tde/HTML/pt/tdeioslave/
%lang(pt_BR) %{tde_prefix}/share/doc/tde/HTML/pt_BR/tdeioslave/
%lang(ro) %{tde_prefix}/share/doc/tde/HTML/ro/tdeioslave/
%lang(ru) %{tde_prefix}/share/doc/tde/HTML/ru/tdeioslave/
%lang(sk) %{tde_prefix}/share/doc/tde/HTML/sk/tdeioslave/
%lang(sr) %{tde_prefix}/share/doc/tde/HTML/sr/tdeioslave/
%lang(sr@Latn) %{tde_prefix}/share/doc/tde/HTML/sr@Latn/tdeioslave/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/tdeioslave/
%lang(uk) %{tde_prefix}/share/doc/tde/HTML/uk/tdeioslave/

